if args[0].startswith("midi"):
	op('select1').par.chop = op(args[6] + '/select1')
	op('select1').par.channames = op(args[6] +'/' + args[0] + '/chanName')[0,0]