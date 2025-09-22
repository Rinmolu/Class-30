class myclass:
    __privatevar = 27
    def __privfunction(self):
        print("This Is A Private Function.")
    def hello(self):
        print("Private Variable Value Is...", myclass.__privatevar)
object1 = myclass()
object1.hello()
object1.__privfunction

