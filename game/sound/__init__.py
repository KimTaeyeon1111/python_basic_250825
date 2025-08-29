# game/sound/__init__.py 

__all__ = ['echo']    
# 터미널 확인 시에 있는 '*'에 모듈을 지정해주어야 '__all__'코드 사용 가능.
# from game.sound import * 이후 all로 모듈을 지정해주면 echo.echo_test()로 사용이 가능하지만 all로 모듈 지정을 안 했을 시에는 오류 발생. 또는 from game.sound.echo import *을 하면 echo_test()처럼 바로 함수를 작성하여도 나온다.