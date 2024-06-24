# ACCAFS

This repository shows an example of using ACCA for evaluating the semantic and syntactic correctness of the code generated by one of the most cutting-edge artificial intelligence models, namely GPT-3.5.

## Theory pills

This example falls within the scope of **Code Generation** and **Prompt Engineering**. 
*Prompt Engineering* is a fundamental practice in the field of natural language processing (NLP), especially when working with large language models such as GPT-3 or GPT-4.
This practice involves designing and optimizing prompts, which are the initial instructions or sentences that are given to a language model to elicit desired responses or specific behaviors. Changing the prompt can help improve the quality and relevance of the answers generated by the model.

*Code Generation* is a process that involves the automatic creation of source code using software or other tools. This process is used in various areas of software engineering to improve efficiency, reduce errors, and standardize software development. Our context is about Code Generation using AI models such as GPT-3, GPT-4 etc. For a model to generate code correctly, two phases are necessary. 

### Training phase

The training phase is the process through which an AI model learns from data. During this phase, the model is exposed to a labeled dataset, and its parameters are optimized to minimize error in its predictions. In this phase data collection, data preprocessing and dataset division take place. In particular, dataset is divided into three main parts: 
* Training set is used to train the model.
* Validation set is used to optimize the model parameters.
* Test set is used to evaluate the final performance of the model.

### Inference phase

The inference phase of a model refers to the process during which the model applies what it has learned (during the training phase) to perform real tasks based on the given input data.

## Experimental process

The goal of the experiment is to use ACCA for evaluating the code generated by ChatGPT-3.5. We will therefore focus only on the inference phase of the model without considering the training phase. Therefore, we will consider GPT-3.5 as a *black-box* and evaluate its output according to the input. 
The experimental process consists of various steps:

### Step 1: ACCA and Installation Guide

*ACCA* (Automating the Correctness Assessment of AI-generated Code for Security Contexts) is a fully automated method to evaluate the correctness of AI-generated code for security purposes. The method uses symbolic execution to assess whether the AI-generated code behaves as a reference implementation, demonstrating a very strong correlation with human-based evaluation, which is considered the ground truth for the assessment in the field.
ACCA works on both Windows and Linux OS and it is strongly recommended to set up an *anaconda* virtual environment, for the installation.

#### Python Setup

Ensure you have Anaconda3 installed, if not install **Python 3.7** from [*Anaconda*](https://www.anaconda.com) with the following steps:
* Install the list of dependencies described [here](https://docs.anaconda.com/anaconda/install/linux/).
* Download the installer [here](https://repo.anaconda.com/archive/). For example, you can use the `wget` command: `wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh`, then type `chmod +x Anaconda3-2021.05-Linux-x86_64.sh` and run `bash Anaconda3-2021.05-Linux-x86_64.sh` to complete the installation.
* You may need to add *anaconda directory* to the PATH environment variable (e.g., you can add `export PATH="/path_to_anaconda/anaconda3/bin:$PATH"` to the `bashrc` file).

#### Dependencies Setup

* Create an anaconda Python 3.7 virtual environment using the command ``conda create -n yourenvname python=3.7``.  
* Activate the environment by typing ``source activate yourenvname``.
* Run ``pip install -r requirements.txt --user`` to install the dependencies.

#### NASM assembler Setup

* To perform the automatic evaluation of syntactic and semantic correctness of the code snippets generated by the NMT models, you need to set up the NASM assembler. To download and install NASM (version 2.15.05), run the following command `./nasm_setup.sh`.

### Step 2: Dataset

[Here](https://github.com/dessertlab/ESCAPE/tree/main/datasets/shellcode_ia32_extended) it is possible to extract a subset of intent/snippet pairs which will constitute the starting dataset. Download only the `assembly-test.in` and `assembly-test.out` files. The first contains all the descriptions in natural language. The second contains all the Assembly language codes that represent the *Ground Truth*.

### Step 3: Creating prompt

In the context of Prompt Engineering, it is essential to create correct and precise prompts to obtain as many answers from the specific model. In this experiment, the goal is to ask ChatGPT-3.5 to generate Assembly language codes, given natural language descriptions. When constructing the prompt it is necessary to specify the structure of the code so that it is generated in the correct form. Finally, it is necessary to specify that the generated code must be extracted in a simple way.

> [!CAUTION]
> Pay attention to the structure of the code snippets. As you can see from the previously downloaded `assembly-test.out` file, the Assembly codes are all *single-line*. In fact, multi-line instructions are separated from each other with `\n`.

In the following folder there is the prompt submitted to ChatGPT for the creation of Assembly codes:

### Step 3: Prompt submission

Once created, you need to prompt the model. Then log in to ChatGPT (https://chatgpt.com/), paste the prompt and hit enter.


> [!WARNING]
> It is recommended to use a subset of samples (~50/100 samples) to submit to the model so that it responds correctly without making errors. If you want to consider the entire dataset (590 samples), then it is possible to send the descriptions in natural language with a rate of 50-100 intents at a time. This will avoid any model errors in code generation. 

> [!NOTE]
> Errors such as sample overlap, incorrect code generation, slow loading etc may be due to the length of the submitted prompt and the amount of data to be processed. Consequently, it is recommended to *refresh* the page after 3 submissions.

### Step 4: Save the output

Given the input to the model, it is necessary to save the output in the same form as the `assembly-test.out` file.

### Step 5: Using ACCA

Once the complete output has been saved, everything is now ready to use *ACCA*. Access the repository [here](https://github.com/dessertlab/ACCA/tree/main) and clone it with the command `gh repo clone dessertlab/ACCA`. 
This repository contains:
1. The source code for *ACCA* and references file and predictions file to perform the semantic evaluation of AI-generated code and replicate our empirical analysis. The folder also contains a [README.md](https://github.com/dessertlab/ACCA/blob/main/ACCA/README.md) file explaining how to run the code and how to test *ACCA* on a different pair of references and predictions files. (``ACCA`` folder).
2. The files necessary for setting up the working environment, including the NASM assembler (``requirements.txt`` and ``nasm_setup.sh``).
3. The results we obtained by evaluating the code generated by five AI models encompassed in our analysis, i.e., Seq2Seq, CodeBERT, CodeT5+, PLBart and ChatGPT-3.5. The folder contains an XLSX file with the results of our empirical analysis and a [README.md](https://github.com/dessertlab/ACCA/blob/main/Experimental%20Results/README.md) file describing how to interpret the results (``Experimental Results`` folder).
Access the ACCA folder. To correctly perform the evaluation, make sure to follow these steps:

#### Ground Truth and Predictions Files Setup

* Put the file containing your ground truth code snippets in the ``Ground Truth and Predictions/Ground Truth`` folder.
* Put the file containing your predicted code snippets in the ``Ground Truth and Predictions/Predictions`` folder.

#### Syntactic Correctness Analysis
	
* To perform the syntactic evaluation, run the command ``python syntactic_analisys.py``. The script opens up a window that lets you select the file to evaluate. 

#### Semantic Correctness Analysis 

* To perform the semantic evaluation, run the command ``python semantic_analisys.py``. The script opens up a window that lets you select the file to evaluate. Make sure to select the file containing the results of the previous syntactic analysis.

### Step 6: Metrics

Through the script `` output_similarity_metrics_best `` it is possible to calculate some metrics as described in [README.md](https://github.com/dessertlab/ACCA/blob/main/Experimental%20Results/README.md).

### Step 7: Results

The results can be stored in a manually compiled excel file such as [here](https://github.com/dessertlab/ACCA/blob/main/Experimental%20Results/Results.xlsx).
* The results of the semantic analysis are both shown and stored in a .csv file in the ``Output/Output_Semantic_Analysis`` folder.
* The results of the syntactic analysis are both shown and stored in a .csv file in the ``Output/Output_Syntactic_Analysis`` folder. In the ``Filtered Snippets`` folder you can also find the results filtered by warnings, undefined symbol errors and other errors.

















