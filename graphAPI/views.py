from templates import app
from flask import render_template, Blueprint, jsonify, json, send_from_directory, Flask, make_response, request
import requests
import json
import os
from gremlin_python.driver import client, serializer
from flask_restplus import Api, apidoc, Resource, fields, reqparse
from neo4jrestclient.client import GraphDatabase

graphAPI_blueprint = Blueprint('graph_api', __name__, url_prefix='/graph_api')
api = Api(graphAPI_blueprint, version='1.0', title='Graph API AI Ecosystem PoC',
          description="Graph DB's query API first draft for discussion purpouses.")
name_space = api.namespace('', description='Graph API')

irc_item = api.model('Internal Revenue Code item',
                     {'sec': fields.String(required=True, description="Name of the person", help="Name cannot be blank.")})

idModel = api.model('ID Model to get the Node', {
    'sec': fields.String(required=True, description="Section Number"),
    'subsec': fields.String(required=False, description="Subsection Number"),
    'par': fields.String(required=False, description="Paragraph Number"),
    'subpar': fields.String(required=False, description="Subparagraph Number"),
    'cls': fields.String(required=False, description="Clause Number"),
    'subcls': fields.String(required=False, description="Subclause Number")
})


pagination = reqparse.RequestParser()
pagination.add_argument('sec', type='string', required=True)
pagination.add_argument('subsec', type='string', required=False)
pagination.add_argument('par', type='string', required=False)
pagination.add_argument('subpar', type='string', required=False)
pagination.add_argument('cls', type='string', required=False)
pagination.add_argument('subcls', type='string', required=False)

n4j = {
    'url': 'http://localhost:7474',
    'usr': 'neo4j',
    'psw': 'ignacio',
}
graph = GraphDatabase(n4j['url'], n4j['usr'], n4j['psw'])


def cleanText(text):
    txt = text
    txt_clean = txt.replace('>', '').replace("'", '').replace("}", '')
    return txt_clean


def findId(sec, subsec, par, subpar, clsn, subcls):
    try:
        if sec:
            if subsec:
                if par:
                    if subpar:
                        if clsn:
                            if subcls:
                                query = '''MATCH (section { num: "'''+str(sec)+'''" })--
                                (subsection { num: "'''+subsec+'''"})--
                                (paragraph { num: "'''+str(int(par))+'''"})--
                                (subparagraph { num: "'''+subpar+'''"})--
                                (clause { num: "'''+clsn+'''"})--
                                (subclause { num: "'''+subcls+'''"})
                                RETURN subclause
                                LIMIT 1'''
                            else:
                                query = '''MATCH (section { num: "'''+str(sec)+'''" })--
                                (subsection { num: "'''+subsec+'''"})--
                                (paragraph { num: "'''+str(int(par))+'''"})--
                                (subparagraph { num: "'''+subpar+'''"})--
                                (clause { num: "'''+clsn+'''"})
                                RETURN clause
                                LIMIT 1'''
                        else:
                            query = '''MATCH (section { num: "'''+str(sec)+'''" })--
                            (subsection { num: "'''+subsec+'''"})--
                            (paragraph { num: "'''+str(int(par))+'''"})--
                            (subparagraph { num: "'''+subpar+'''"})
                            RETURN subparagraph
                            LIMIT 1'''
                    else:
                        query = '''MATCH (section { num: "'''+str(sec)+'''" })--
                        (subsection { num: "'''+subsec+'''"})--
                        (paragraph { num: "'''+str(int(par))+'''"})
                        RETURN paragraph
                        LIMIT 1'''
                else:
                    query = '''MATCH (section { num: "'''+str(sec)+'''" })--
                    (subsection { num: "'''+subsec+'''"})
                    RETURN subsection
                    LIMIT 1'''
            else:
                query = '''MATCH (n:section) WHERE n.num = "''' + \
                    str(sec)+'''" RETURN n LIMIT 1'''
        else:
            query = '''MATCH (n:section) WHERE n.num = "''' + \
                    str(sec)+'''" RETURN n LIMIT 1'''

        result = graph.query(query)
        for e in result.elements:
            e_json = e[0]
            neoid = e_json['metadata']['id']
            labels = e_json['metadata']['labels']
            print(neoid)
        return neoid
    except:
        return -1


def findNeighsID(contentRes):
    if contentRes:
        list_neighbors_ID = set([])
        for value in contentRes:
            list_neighbors_ID.add(value['nodeOutId'])
    return list_neighbors_ID


"""
URI :
"""
@name_space.route('/RelatedOffering', endpoint='my-resource')
class MyResource(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(pagination, validate=True)
    def get(self):
        try:
            sec = request.args.get('sec')
            subsec = request.args.get('subsec')
            par = request.args.get('par')
            subpar = request.args.get('subpar')
            clsn = request.args.get('clsn')
            subcls = request.args.get('subcls')

            IDtemp = findId(sec, subsec, par, subpar, clsn, subcls)

            if IDtemp:
                query = "MATCH (n)-[r:USES]-(m:offering) WHERE ID(n)=" + \
                    str(IDtemp)+" RETURN m"
                print(query)
            else:
                return make_response(jsonify({'message': 'ID not found'}), 403)

            result = graph.query(query)
            offerings = []
            for e in result.elements:
                e_json = e[0]
                print(e_json)
                neoid = e_json['metadata']['id']
                labels = e_json['metadata']['labels']
                uuid = e_json['data']['uuid']
                name = e_json['data']['name']
                off = {'id': neoid, 'labels': labels,
                       'uuid': uuid, 'name': name}
                offerings.append(off)
            return make_response(jsonify(offerings), 200)
        except:
            return make_response(jsonify({'message': 'Offering not found'}), 403)


"""
URI : getNode/<id of the node>
Using this to get the properties of a single node.
"""
@name_space.route('/getNode/<path:id>', endpoint='get-node')
class GetNode(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, params={'id': "Get an specific node using it's ID"})
    def get(self, id):
        try:
            node = graph.nodes.get(id)
            json_node = []
            json_node.append(
                {'id': node.id, 'properties': node.properties})
            return make_response(jsonify(json_node), 200)
        except:
            return make_response(jsonify({'message': 'Node not Found'}), 403)


"""
URI : getRelationship/<id of the node>
Using this to get all the relationships of the Node.
"""
@name_space.route('/getRelationship/<path:id>', endpoint='get-relation')
class GetRelationship(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, params={'id': "Get an specific relationship using it's ID"})
    def get(self, id):
        try:
            node = graph.nodes.get(id)
            if node:
                relationships = node.relationships.all()
                json_re = []
                for r in relationships:
                    nodeStart = r.start
                    nodeEnd = r.end
                    label = nodeStart.labels
                    txt_clean = cleanText(label.__unicode__()[15:])
                    json_re.append({'idRelation': r.id, 'nodeOutId': nodeEnd.id, 'labels': txt_clean, 'properties': r.properties, 'type': r.type, 'nodeIn': nodeStart.properties,
                                    'nodeOut': nodeEnd.properties})
                return make_response(jsonify(json_re), 200)
        except:
            return make_response(jsonify({'message': 'Node not Found'}), 403)


"""
URI : getRelationship/<id of the node>
Using this to get all the relationships of the Node.
"""
@name_space.route('/getOffersRelated/<path:title>', endpoint='get-offer-related')
class GetOfferRelated(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, params={'title': "Get offers related using it's name"})
    def get(self, title):
        try:
            result = graph.query(
                'MATCH (n: offering)-[:USES]-()-[:USES]-(ofer: offering) WHERE n.name="'+title+'" RETURN DISTINCT ofer')
            json_re = []

            for e in result.elements:
                e_json = e[0]
                neoid = e_json['data']['uuid']
                labels = e_json['metadata']['labels']
                name = e_json['data']['name']
                json_re.append({'id': neoid, 'label':  labels, 'name': name})

            if json_re:
                return make_response(jsonify(json_re), 200)
            else:
                return make_response(jsonify({'message': 'Offer not found'}), 403)
        except:
            return make_response(jsonify({'message': 'Node not Found or you just wrote bad the name'}), 403)


"""
URI : /getID/<path:id>/<path:subsec>/<path:par>/<path:subpar>/<path:cls>/<path:subcls>
Use this to get the ID of one Node.
"""
@name_space.route('/getID', endpoint='get-id')
class getID(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(pagination, validate=True)
    def get(self):
        sec = request.args.get('sec')
        subsec = request.args.get('subsec')
        par = request.args.get('par')
        subpar = request.args.get('subpar')
        clsn = request.args.get('clsn')
        subcls = request.args.get('subcls')
        print(sec, subsec, par, subpar, clsn, subcls)
        try:
            if sec:
                if subsec:
                    if par:
                        if subpar:
                            if clsn:
                                if subcls:
                                    query = '''MATCH (section { num: "'''+str(sec)+'''" })--
                                    (subsection { num: "'''+subsec+'''"})--
                                    (paragraph { num: "'''+str(int(par))+'''"})--
                                    (subparagraph { num: "'''+subpar+'''"})--
                                    (clause { num: "'''+clsn+'''"})--
                                    (subclause { num: "'''+subcls+'''"})
                                    RETURN subclause
                                    LIMIT 1'''
                                else:
                                    query = '''MATCH (section { num: "'''+str(sec)+'''" })--
                                    (subsection { num: "'''+subsec+'''"})--
                                    (paragraph { num: "'''+str(int(par))+'''"})--
                                    (subparagraph { num: "'''+subpar+'''"})--
                                    (clause { num: "'''+clsn+'''"})
                                    RETURN clause
                                    LIMIT 1'''
                            else:
                                query = '''MATCH (section { num: "'''+str(sec)+'''" })--
                                (subsection { num: "'''+subsec+'''"})--
                                (paragraph { num: "'''+str(int(par))+'''"})--
                                (subparagraph { num: "'''+subpar+'''"})
                                RETURN subparagraph
                                LIMIT 1'''
                        else:
                            query = '''MATCH (section { num: "'''+str(sec)+'''" })--
                            (subsection { num: "'''+subsec+'''"})--
                            (paragraph { num: "'''+str(int(par))+'''"})
                            RETURN paragraph
                            LIMIT 1'''
                    else:
                        query = '''MATCH (section { num: "'''+str(sec)+'''" })--
                        (subsection { num: "'''+subsec+'''"})
                        RETURN subsection
                        LIMIT 1'''
                else:
                    query = '''MATCH (n:section) WHERE n.num = "''' + \
                        str(sec)+'''" RETURN n LIMIT 1'''
            else:
                query = '''MATCH (n:section) WHERE n.num = "''' + \
                    str(sec)+'''" RETURN n LIMIT 1'''

            result = graph.query(query)
            for e in result.elements:
                e_json = e[0]
                neoid = e_json['metadata']['id']
                labels = e_json['metadata']['labels']
                print(neoid)
            return make_response(jsonify({'idNode': neoid, 'labels': labels}), 200)
        except:
            return make_response(jsonify({'message': 'Node not found'}), 403)
