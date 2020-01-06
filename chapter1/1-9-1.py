###1  エラーが起きた。以下、実行したプログラムとエラー文

#>>>print('hello')

#  File "<stdin>", line 1
#    print 'hello'
                ^
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello')?


###2 エラーが起きた。以下、実行したプログラムとエラー文

#>>>print('hello)

#  File "<stdin>", line 1
#    print ('hello)
                 ^
#SyntaxError: EOL while scanning string literal


###3 どちらも正の符号として認識された


###4 エラーが起きた。以下、実行したプログラムとエラー文

#>>>01

#  File "<stdin>", line 1
#    01
     ^
#SyntaxError: invalid token


###5 エラーが起きた。以下、実行したプログラムとエラー文

#>>> 1 2

#  File "<stdin>", line 1
#    1 2
#      ^
#SyntaxError: invalid syntax