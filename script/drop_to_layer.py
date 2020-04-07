#print(args)

if args[5] == 'COMP':
	outTop = op('null')

	m = op('movie')
	t = op('tox')

	fromPath = args[6] + '/' + args[0]

	type = op(fromPath + '/info')[1, 'type']
	path = op(fromPath + '/info')[1, 'path']
	
	parent().par.Mediatype = type
	
	op('display_select').par.top = fromPath + '/display'
	op(fromPath).op('movie').par.cuepulse.pulse()