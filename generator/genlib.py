import os

class ioData:
    def __init__(self, input, output):
        self.input = input
        self.output = output
        
def generate(fileName, dataList):
    link = fileName.replace(' ', '-')

    file = open( f'{os.path.dirname(__file__)}/../data/{fileName}.md', 'w' )
    file.write( f'# {fileName} ex)\n\n' )
    file.write( f'* [문제로 돌아가기](../problems.md#{ link })\n' )
    file.write( '---\n\n' )

    for index in range(len(dataList)):
        file.write( f'### 입력 {index + 1}\n' )
        file.write( '```\n' )
        file.write( f'{dataList[index].input}\n' )
        file.write( '```\n' )

        file.write( f'### 출력 {index + 1}\n' )
        file.write( '```\n' )
        file.write( f'{dataList[index].output}\n' )
        file.write( '```\n\n' )

        file.write( '---\n\n' )

    file.write( f'* [문제로 돌아가기](../problems.md#{ link })\n' )
    file.close()

    print(f'{fileName}.md data generated')