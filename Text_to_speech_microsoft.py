import os, requests, time
from xml.etree import ElementTree
import textwrap
import threading
from pydub import AudioSegment
import os 
import glob

try: input = raw_input
except NameError: pass



class TextToSpeech(object):
	def __init__(self, subscription_key,chunk):
	    self.subscription_key = subscription_key
	    #self.tts = input("What would you like to convert to speech: ")
	    #self.tts = '11. CPA Notice; PwC Related Parties; Nature of Engagement. PwC is owned by professionals who hold CPA licenses as well as by professionals who are not licensed CPAs. Depending on the nature of the products and services provided to you under this Agreement (including the Solution or through the Solution), non-CPA owners may be involved in providing such products and services. PwC is a firm in the global network of separate and independent PricewaterhouseCoopers firms (exclusive of PwC, the “Other PwC Firms”). PwC may draw on the resources of (and subcontract to) its affiliates, the Other PwC Firms and third party contractors and subcontractors, within or outside of the United States (each, a “PwC Service Provider”) for internal, administrative and regulatory compliance purposes or in connection with providing the Solution. The PwC Service Providers and their and PwC’s respective partners, principals, employees and agents (collectively, the “PwC Beneficiaries”) will have no liability or obligations arising out of this Agreement, and you agree to bring any claim or other legal proceeding of any nature arising from or related to this Agreement or its subject matter against PwC and not against the PwC Beneficiaries. While PwC is entering into this Agreement on its own behalf, this Section 11 also is intended for the benefit of the PwC Beneficiaries. This Solution does not include, and is not intended to constitute, tax advice and, therefore, is not subject to Treasury Department Circular 230 and/or Internal Revenue Code § 6694. Any services requested by you, or proposed by PwC, that would constitute tax advice will be provided under a separate engagement letter, including appropriate terms and conditions, with PricewaterhouseCoopers LLP.'
	    self.tts = chunk
	    self.timestr = time.strftime("%Y%m%d-%H%M%S")
	    self.access_token = None

	def save_audio(self):
	    base_url = 'https://westus.tts.speech.microsoft.com/'
	    path = 'cognitiveservices/v1'
	    constructed_url = base_url + path
	    headers = {
	        'Authorization': 'Bearer ' + self.access_token,
	        'Content-Type': 'application/ssml+xml',
	        'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
	        'User-Agent': 'martin.x.lujan@pwc.com'
	    }
	    xml_body = ElementTree.Element('speak', version='1.0')
	    xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
	    voice = ElementTree.SubElement(xml_body, 'voice')
	    voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
	    #voice.set('name', 'Microsoft Server Speech Text to Speech Voice (en-US, Guy24KRUS)')
	    voice.set('name', 'Microsoft Server Speech Text to Speech Voice (en-US, Jessa24kRUS)')
	    voice.text = self.tts
	    body = ElementTree.tostring(xml_body)

	    response = requests.post(constructed_url, headers=headers, data=body)
	    if response.status_code == 200:
	        with open('sample-' + self.timestr + '.wav', 'wb') as audio:
	            audio.write(response.content)
	            print("\nStatus code: " + str(response.status_code) + "\nYour TTS is ready for playback.\n")
	    else:
	        print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")

	def get_token(self):
	    fetch_token_url = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
	    headers = {
	        'Ocp-Apim-Subscription-Key': self.subscription_key
	    }
	    response = requests.post(fetch_token_url, headers=headers)
	    self.access_token = str(response.text)

if __name__ == "__main__":
    subscription_key = "70a63dee4aa64903aad34599284b3195"

    


    txt= open('article134.txt','r').read()
    wrapper = textwrap.TextWrapper(width=1024)

    wrapped_txt = wrapper.wrap(text=txt)

    def funct(chunk):
        app = TextToSpeech(subscription_key,chunk)
        app.get_token()
        app.save_audio()

    for chunk in wrapped_txt :

        thread = threading.Thread(target=funct,
                                      args=[chunk])
        thread.start()
        thread.join()

    for idx,file in enumerate(sorted(glob.glob('sample-*.wav'))):
    	if idx == 0:
    		final = AudioSegment.from_file(file,'wav')
    	else:

    		final += AudioSegment.from_file(file,'wav') 
    

    

    final.export('mashup_article_134.wav',format='wav')

	





#Endpoint: https://westus.api.cognitive.microsoft.com/sts/v1.0

#Key 1: 95e76fe2b6d549508f3a95bf005962ae

#Key 2: 70a63dee4aa64903aad34599284b3195

