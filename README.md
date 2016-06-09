# py-one-chat
Wrapper for all available chat messaging SEND api (like Facebook, Twillio, ...)

## Current State
Currently, it supports Facebook messages of the following type:
1. Text Message
2. Image Message
3. Generic Message
4. Button Message

## Usage
To setup:
```
import onechat
from onechat.client import Client
from onechat.message import *

client = Client("config.txt")
recepient = client.config.get('onechat','RECEPIENT')
```

For Facebook Text Message:
```
message = FacebookTextMessage("test")
response = client.send(recepient, message)
```

For Facebook Image Message:
```
message = FacebookImageMessage("http://some.image.com")
response = client.send(recepient, message)
```

For Facebook Button Message:
```
facebookButtonsInfo = FacebookButtonsInfo(\
			types=["web_url","postback","web_url"], \
			titles=["Button A", "Button B", "Button C"],\
			urlsOrPayloads=["http://www.build2master.com", "B", "http://www.build2master.com"])

message = FacebookButtonMessage("A, B or C?", facebookButtonsInfo)
response = client.send(recepient, message)
```

For Facebook Generic Template:
```
facebookButtonsInfo = FacebookButtonsInfo(\
			types=["web_url","postback","web_url"], \
			titles=["Button A", "Button B", "Button C"],\
			urlsOrPayloads=["http://www.build2master.com", "B", "http://www.build2master.com"])
		
facebookGenericElement1 = FacebookGenericElement(\
			title="Element Title 1", item_url="http://www.build2master.com",\
			image_url="http://www.build2master.com/uploads/3/7/3/4/37345271/7877270.png",\
			subtitle="Build-2-Master has awesome articles", buttons=facebookButtonsInfo)
		
facebookGenericElement2 = FacebookGenericElement(title="Element Title 2",subtitle="Great!")
		
facebookGenericElements = [facebookGenericElement1, facebookGenericElement2]
		
message = FacebookGenericMessage(facebookGenericElements)
response = client.send(recepient, message)
```

## Future plans
To support Facebook Messenger's Receipt templates.
Also, we are consider to support Twillio.
