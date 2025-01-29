def main():
	count=0
	newcount=0
	acount=0
	bcount=0
	ccount=0
	dcount=0
	ecount=0
	fcount=0
	gcount=0
	hcount=0
	icount=0
	jcount=0
	kcount=0
	lcount=0
	mcount=0
	ncount=0
	ocount=0
	pcount=0
	qcount=0
	rcount=0
	scount=0
	tcount=0
	ucount=0
	vcount=0
	wcount=0
	xcount=0
	ycount=0
	zcount=0
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
		for words in file_contents:
			for letter in words:
				element=letter.lower()
				count+=1
				if element==' ':
					newcount+=1
				if element=='a':
					acount+=1
				if element=='b':
					bcount+=1
				if element=='c':
					ccount+=1
				if element=='d':
					dcount+=1
				if element=='e':
					ecount+=1
				if element=='f':
					fcount+=1
				if element=='g':
					gcount+=1
				if element=='h':
					hcount+=1
				if element=='i':
					icount+=1
				if element=='j':
					jcount+=1
				if element=='k':
					kcount+=1
				if element=='l':
					lcount+=1
				if element=='m':
					mcount+=1
				if element=='n':
					ncount+=1
				if element=='o':
					ocount+=1
				if element=='p':
					pcount+=1
				if element=='q':
					qcount+=1
				if element=='r':
					rcount+=1
				if element=='s':
					scount+=1
				if element=='t':
					tcount+=1
				if element=='u':
					ucount+=1
				if element=='v':
					vcount+=1
				if element=='w':
					wcount+=1
				if element=='x':
					xcount+=1
				if element=='y':
					ycount+=1
				if element=='z':
					zcount+=1

	#print(f'\'p\':{pcount},\'c\':{ccount},\' \':{newcount}')
	print(f'There are {count} words with unique letter count at: \' \': {newcount},\'a\': {acount},\'b\': {bcount},\'c\': {ccount},\'d\': {dcount},\'e\': {ecount}, \'f\': {fcount},\'g\': {gcount},\'h\': {hcount},\'i\': {icount},\'j\': {jcount},\'k\': {kcount},\'l\': {lcount},\'m\': {mcount},\'n\': {ncount},\'o\': {ocount},\'p\': {pcount},\'q\': {qcount},\'r\': {rcount},\'s\': {scount},\'t\': {tcount},\'u\': {ucount},\'v\': {vcount},\'w\': {wcount},\'x\': {xcount},\'y\': {ycount},\'z\': {zcount}')

main()
