# LLM-based Blog Generation with Streamlit Interface

Welcome to the LLM-based Blog Generation project repository! This project utilizes advanced language modeling techniques, specifically the LLaMA 2 model, to generate high-quality blog content based on user-selected topics. The generated blogs are tailored to meet user-specified word limits and are accessible through a user-friendly Streamlit interface. Additionally, Langchain integration ensures transparency and integrity in content management.

## Installation

To set up the project environment, follow these steps:

1. Clone this repository to your local machine.
2. Install the required Python libraries by running:
    ```bash
    pip install -r requirements.txt
    ```

## Model Download

Download the LLaMA 2 model from [here](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML) and place it in the `models` folder in your local project directory.

## Usage

To run the Streamlit app and generate blogs, execute the following command in your terminal:

```bash
streamlit run app.py
```
## input screen
![input screen](https://github.com/fenil210/LLM-based-Blog-Generator/assets/121050723/5f42bb9a-10b9-444d-998a-0d9f76453165)


### Once the app is running, navigate to the provided URL in your web browser.
#### Blog Generation
1) Choose a topic/domain from the following options:
  a) Researchers
  b) Data Scientist
  c) Tech Enthusiast
  d) Environmental Activist
  e) Culinary Connoisseur
  f) Movie Critic
  g) Common People

2) Enter the desired word limit for the generated blog.

3) Click on the "Generate Blog" button to initiate the blog generation process.

4) The generated blog will be displayed on the interface, ready for reading or further customization.

## output screen
![output](https://github.com/fenil210/LLM-based-Blog-Generator/assets/121050723/e41318b8-0593-4b89-ac38-12342fd4b4bb)

## Acknowledgements
[Hugging Face](https://huggingface.co/) for providing access to the LLaMA 2 model.

[Streamlit](https://streamlit.io/) for simplifying the development of interactive web applications.

[Langchain](https://www.langchain.com/) for ensuring content integrity through blockchain integration.

[Krish Naik](https://twitter.com/krishnaik06?lang=en) for LLM, Streamlit and Langchain guidance.








