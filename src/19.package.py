# https://wikidocs.net/1418

'''
The example of game package structure
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
'''

# import game.sound.echo
# game.sound.echo.echo_test()

# from game.sound import echo
# echo.echo_test()

# from game.sound.echo import echo_test
# echo_test()

'''
import game
game.sound.echo.echo_test()

Traceback (most recent call last):
  File "src/19.package.py", line 31, in <module>
    game.sound.echo.echo_test()
AttributeError: module 'game' has no attribute 'sound'
'''

'''
import game.sound.echo.echo_test

Traceback (most recent call last):
  File "src/19.package.py", line 40, in <module>
    import game.sound.echo.echo_test
ModuleNotFoundError: No module named 'game.sound.echo.echo_test'; 'game.sound.echo' is not a package
'''

'''
> Before define the __init__.py

from game.sound import *
echo.echo_test()

Traceback (most recent call last):
  File "src/19.package.py", line 50, in <module>
    echo.echo_test()
NameError: name 'echo' is not defined
'''

'''
> After define the __inint__.py
> It's work!

from game.sound import *
echo.echo_test()
'''

from game.graphic.render import render_test
render_test()