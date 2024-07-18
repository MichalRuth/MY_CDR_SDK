# AI_model_CDR_SDK
## AI model CDR SDK
### Project Goals:
#### CDR AI models:
##### Pytorch (existing) 
##### Tensorflow
##### Keras
##### dill & joblib
Detect threats In AI models
`Articles:
https://hiddenlayer.com/research/weaponizing-machine-learning-models-with-ransomware/
https://www.geektime.co.il/malicious-hugging-face-ml-models/?utm_source=whatsapp&utm_medium=social&utm_campaign=share&utm_term=article_page&utm_content=514769
# Repo: 
Attacks:

1) https://github.com/protectai/modelscan/tree/main/notebooks


2) https://github.com/trailofbits/fickling
3) https://github.com/ArielCyber/ModelSerializationCDR
4)  Search more in the web

GitHub - trailofbits/fickling: A Python pickling decompiler and static analyzer
A Python pickling decompiler and static analyzer. Contribute to trailofbits/fickling development by creating an account on GitHub.
github.com


# Steps:
Could you create a report about the file structure of pickle . About the attacks you find on the net and in the repos. Explain the attack stages in detail [ one week]

Learn the attacks for pickle and your model. Document the attacks, how they work, and how we can "remove " the active content of the attack from the model. Please don't regularly load the model. Only throw raw data- it will attack you. Create SDK based on Code API.
[two weeks]
Develop unit tests for each supported attack, attack detection, and attack disarm [four weeks]

# Code API:
model,analysis= model_load(model,type, detect=True,disarm=True) \\ will secure load a model
model_save(model,in_type,out_type) \\ will securely save a model to the out_type (torch, tensor,k5, ONNX, safe-tensor
Prevention Container:
Receive a model and provide the same functionality.

