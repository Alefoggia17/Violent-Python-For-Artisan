# ACCAFS

This repository shows an example of using ACCA for evaluating the semantic and syntactic correctness of the code generated by one of the most cutting-edge artificial intelligence models, namely ChatGPT-3.5.

## ACCA and Installation Guide

*ACCA* (Automating the Correctness Assessment of AI-generated Code for Security Contexts) is a fully automated method to evaluate the correctness of AI-generated code for security purposes. The method uses symbolic execution to assess whether the AI-generated code behaves as a reference implementation, demonstrating a very strong correlation with human-based evaluation, which is considered the ground truth for the assessment in the field.
ACCA works on both Windows and Linux OS and it is strongly recommended to set up an *anaconda* virtual environment, for the installation.

### Step 1: Python Setup

Ensure you have Anaconda3 installed, if not install **Python 3.7** from [*Anaconda*](https://www.anaconda.com) with the following steps:
* Install the list of dependencies described [here](https://docs.anaconda.com/anaconda/install/linux/)
* Download the installer [here](https://repo.anaconda.com/archive/). For example, you can use the `wget` command: `wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh`, then type `chmod +x Anaconda3-2021.05-Linux-x86_64.sh` and run `bash Anaconda3-2021.05-Linux-x86_64.sh` to complete the installation.
* You may need to add *anaconda directory* to the PATH environment variable (e.g., you can add `export PATH="/path_to_anaconda/anaconda3/bin:$PATH"` to the `bashrc` file).

### Step 2: Dependencies Setup

* Create an anaconda Python 3.7 virtual environment using the command ``conda create -n yourenvname python=3.7``.  
* Activate the environment by typing ``source activate yourenvname``.
* Run ``pip install -r requirements.txt --user`` to install the dependencies.

### Step 3: NASM assembler Setup

* To perform the automatic evaluation of syntactic and semantic correctness of the code snippets generated by the NMT models, you need to set up the NASM assembler. To download and install NASM (version 2.15.05), run the following command `./nasm_setup.sh`.

## Prompt Engineering

A fundamental practice in the field of natural language processing (NLP) is *Prompt Engineering*, especially when working with large language models such as GPT-3 or GPT-4.
This practice involves designing and optimizing prompts, which are the initial instructions or sentences that are given to a language model to elicit desired responses or specific behaviors. Changing the prompt can help improve the quality and relevance of the answers generated by the model.

## Experimental process

The goal of the experiment is to use ACCA for evaluating the code generated by ChatGPT-3.5. We will therefore focus only on the inference phase of the model. The *inference phase* of a model refers to the process during which the model applies what it has learned (during the training phase) to perform real tasks based on the given input data. The experimental process consists of various steps.

### Step 1: Dataset

At https://github.com/dessertlab/ESCAPE/tree/main/datasets/shellcode_ia32_extended it is possible to extract a subset of intent/snippet pairs which will constitute the starting dataset. Download only the `assembly-test.in` and `assembly-test.out` files. The first contains all the descriptions in natural language. The second contains all the Assembly language codes related to natural language descriptions.

### Step 2: Creating prompt

In the context of Prompt Engineering, it is essential to create correct and precise prompts to obtain as many answers from the specific model. In this experiment, the goal is to ask ChatGPT-3.5 to generate Assembly language codes, given natural language descriptions. When constructing the prompt it is necessary to specify the structure of the code so that it is generated in the correct form. Finally, it is necessary to specify that the generated code must be extracted in a simple way.

!! PAY ATTENTION !!

Pay attention to the structure of the code snippets. As you can see from the previously downloaded `assembly-test.out` file, the Assembly codes are all *single-line*. In fact, multi-line instructions are separated from each other with `\n`.

In the following folder there is the prompt submitted to ChatGPT for the creation of Assembly codes:

### Step 3: Prompt submission

Once created, you need to prompt the model. 
Then log in to ChatGPT (https://chatgpt.com/), paste the prompt and hit enter.

!! PAY ATTENTION !!

It is recommended to use a subset of samples (~50/100 samples) to submit to the model so that it responds correctly without making errors. If you want to consider the entire dataset (590 samples), then it is possible to send the descriptions in natural language with a rate of 50-100 intents at a time. This will avoid any model errors in code generation. 
*Please note*: errors such as sample overlap, incorrect code generation, slow loading etc may be due to the length of the submitted prompt and the amount of data to be processed. Consequently, it is recommended to *refresh* the page after 3 submissions.

### Step 4: Save the output

Given the input to the model, it is necessary to save the output in the same form as the `assembly-test.out` file.

### Step 5: Using ACCA

Once the complete output has been saved, everything is now ready to use *ACCA*. Access the repository https://github.com/dessertlab/ACCA/tree/main and clone with the command `gh repo clone dessertlab/ACCA`). This repository contains:
1. The source code for *ACCA* and references file and predictions file to perform the semantic evaluation of AI-generated code and replicate our empirical analysis. The folder also contains a [README.md](https://github.com/dessertlab/ACCA/blob/main/ACCA/README.md) file explaining how to run the code and how to test *ACCA* on a different pair of references and predictions files. (``ACCA`` folder).
2. The files necessary for setting up the working environment, including the NASM assembler (``requirements.txt`` and ``nasm_setup.sh``).
3. The results we obtained by evaluating the code generated by five AI models encompassed in our analysis, i.e., Seq2Seq, CodeBERT, CodeT5+, PLBart and ChatGPT-3.5. The folder contains an XLSX file with the results of our empirical analysis and a [README.md](https://github.com/dessertlab/ACCA/blob/main/Experimental%20Results/README.md) file describing how to interpret the results (``Experimental Results`` folder).
Access the ACCA folder. To correctly perform the evaluation, make sure to follow these steps:

#### Step 0: Ground Truth and Predictions Files Setup

* Put the file containing your ground truth code snippets in the ``Ground Truth and Predictions/Ground Truth`` folder
* Put the file containing your predicted code snippets in the ``Ground Truth and Predictions/Predictions`` folder

#### Step 1: Syntactic Correctness Analysis
	
* To perform the syntactic evaluation, run the command ``python syntactic_analisys.py``. The script opens up a window that lets you select the file to evaluate. 
* The results of the syntactic analysis are both shown and stored in a .csv file in the ``Output/Output_Syntactic_Analysis`` folder. In the ``Filtered Snippets`` folder you can also find the results filtered by warnings, undefined symbol errors and other errors.

#### Step 2: Semantic Correctness Analysis 

* To perform the syntactic evaluation, run the command ``python semantic_analisys.py``. The script opens up a window that lets you select the file to evaluate. Make sure to select the file containing the results of the previous syntactic analysis.
* The results of the semantic analysis are both shown and stored in a .csv file in the ``Output/Output_Semantic_Analysis`` folder.

### Step 6: Results
















