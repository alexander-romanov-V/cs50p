emoteicon = ":("

def main():
    global emoteicon                    # explicitly declared to modify global var inside function
    say("Is anyone there?")
    emoteicon = ":D"                    # by default it will be another local var (to modify it needs to be explicit defined as 'global')
    say("Oh, hi!")

def say(phrase):
    print(phrase + " " + emoteicon)     # we can access to global var anytime

main()