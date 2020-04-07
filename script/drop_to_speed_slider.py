#print(args)

if args[5] == 'COMP':
	if args[0].startswith('midi') == True:
		op('speed_slider/selectMIDI').par.chop = op(args[6] + '/' + args[0] + '/midi_value')
		op('speed_slider/selectMIDI').par.channames = '*'