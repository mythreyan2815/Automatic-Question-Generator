import aqgFunction
import nltk
nltk.download('punkt')




    # Main Function
def main():
        # Create AQG object
        aqg = aqgFunction.AutomaticQuestionGenerator()

        # Enter input Text File PATH
        inputTextPath = r"D:\Hinfo\Task_5\Automatic-Question-Generator\input.txt"
        readFile = open(inputTextPath, 'r+')
        inputText = readFile.read()


        questionList = aqg.aqgParse(inputText)
        aqg.display(questionList)

        return 0


    # Call Main Function
if __name__ == "__main__":
        main()
 