# Affective Creative Adverserial Network
### Description:
1. wikiart_subset:
    The wikiart_subset folder consists of the following art style: [Analytica_Cubism, Cubism, Expressionism, Fauvism, Synthetic_Cubism] and consists of 10231
    artworks for testing generative models.
    This folder is not included in the repo, but can be downloaded from https://drive.google.com/drive/folders/1Zg-1Ax32rG3L3xqR_5bwmiHQzlH4CR6h?usp=sharing
    
2. artemis:
    The artemis folder is the copy of original repo by Panos https://github.com/optas/artemis. Please follow the installation guide (step 1-2) on in the original   
    repo to ensure dependecies are installed and so that a deep cleaned .csv file of the emotional reponses to train neural networks on can be obtained. There are 3
    version of the emotion annotated art data provided in artemis: 1) raw (uncleaned), 2) slight cleaning and 3) deep cleaned (used for training neural nets in the         
    original paper).
    
3. notebooks:
    Currently slight adjustment to the notebook folder was made to accomodate the wikiart_subset data for 1) selecting a random artwork and depicting its emotional
    response and 2) select a random artwork based on a genre i.e. portrait, landscape etc.
    
 
### Tasks:
- [ ] Artemis repo working - [all members]
- [ ] DC GAN using wiki_subset - [Deniz]
- [ ] CAN using wiki_subset or original - [Arian]
- [ ] Text Conditioned GAN
- [ ] NLP
