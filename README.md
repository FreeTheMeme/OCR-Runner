The basic goal of this tool is to extract text from images via a web interface or an Android app. 


how it would work a image would be sent to an [OCR model](https://ollama.com/library/glm-ocr) via [ollama api](https://docs.ollama.com/api/introduction) and send back plan text the web interface would be powered by Python in flask


## how to run it locally

docker compose up -d
docker compose exec ollama ollama pull glm-ocr
docker compose exec ollama ollama list