# ai-detector-composite
ai detector composite (adc for short) is a tool that automatically runs a provided text through multiple AI detectors : ZeroGPT, Grammarly, Quillbot, Hive, Writer. There is a wide variation in responses between different sites such as ZeroGPT might predict 5% AI while Quillbot thinks the same text is 60% AI, so this is your all in one ai detector tool to see what each site detects without having to manually go to each site and input your text, and wait for a response. 

## Installation

```bash
git clone https://github.com/johnsony0/ai-detector-composite-.git
pip install playweight==1.47.0
cd ai-detector-composite-
```

## Usage

### CLI
```bash
python main.py [-h] [--headless] [--timeout TIMEOUT]
```
Run `python main.py -h` for more details on each option.

Use `--headless` if you wish for the script to run in the background

Use `--timeout VALUE` to set a limit on how long the browser will wait for certain actions to complete before throwing an error. Default is 15000 (15s) . 

Following the CLI usage you will be prompted to enter the text, you can copy and paste it but if given a warning, make sure to select 'paste in one line'.

### Examples

Running in headless mode with a prompt of 'hello world'
```
> python main.py --headless
Please enter the text you want to analyze: <User Input: Hello World>

```
To run in headless mode and give the browser 60000 seconds to try an action before throwing an error.

```
> python main.py --headless --timeout 60000
```


## Known Issues

1. When using ZeroGPT if the AI influence is predicted to be 0%, it throws an error. (Due to the html element of the 0% to be different than if it has a percentage, works majority of the time though)
2. Grammarly can sometimes take forever to make an inference. Currently I have it wait 10 seconds for the inference, but on really rare occasions, it fail.
3. Quillbot randomly removes the pasted text sometimes.
4. Hive can sometimes have a captcha.
5. Quillbot and Hive have the highest failure rates, ZeroGPT, Writer, and Grammarly almost always works. 

