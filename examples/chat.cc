run = 1

while run == 1 {
	inp = input
	if inp == "hello" {
		print "hi"
	}
	elif inp == "stop" {
		print "stopping"
		run = 0
	}
	else {
		print "I do not understand"
	}
}