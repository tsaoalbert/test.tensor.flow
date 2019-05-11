class wolves_and_sheep (object):
		def count( self ):
		    cnt = 0
		    n = len ( self.board)
		    for i in range ( n): 
		        for j in range ( n):
		            if (self.board[i][j]==0):
		                cnt += 1
		    return cnt
		
		def display( self ):
		  n = 1
		  gap = " "*n
		  offset = " " *1
		  header = gap + "1" + gap +"2" +gap + "3" +gap + "4" +gap + "5"
		  print ( offset + "  " + header )
		  symbol = [ "-", "w", "x" ]
		  for i in range (5):
		    print (offset, i+1 , end="")
		    for j in range (5):
		      k = self.board[i][j]
		      print ( gap + symbol[k], end="" )
		    print ("\n"*n, end="")
		
		def markBoard (self, x,y):
		  n = len (self.board[0])
		  for i in range ( n ):
		    if (self.board[i][y]==0):
		      self.board[i][y]=2
		    if (self.board[x][i]==0):
		      self.board[x][i]=2
		
		  for i in range ( -n+1,n,1 ):
		    a = x + i
		    b = y + i
		    if ( 0<=a<n and 0<=b<n and self.board[a][b]==0):
		      self.board[a][b]=2
		    a = x + i
		    b = y - i
		    if ( 0<=a<n and 0<=b<n and self.board[a][b]==0):
		      self.board[a][b]=2
		
		def __init__ ( self ):
		  row = [0]*5
		  self.board = []
		  for i in range (5):
		    self.board += [row.copy() ]
		
		def game (self,s ):
		  s = s.split()
		  dict = { 0:"-", 1:"W", 2:"S" }
		  for z in s:
		    i = int( z[0] ) - 1
		    j = int( z[1] ) - 1
		    self.board[i][j] = 1
		  for z in s:
		    i = int( z[0] ) - 1
		    j = int( z[1] ) - 1
		    self.markBoard (i,j)
		  self.display ( )
		  ans = self.count ()
		  print ("\nThe input is", s)
		  print ("Number of wolves is ", len(s) )
		  print ("Number of safe spots for sheep are ", ans)
		
		def main(self):
		    again = True
		    while again:
		      print ("Game of 5 Wolves and 3 Sheep" )
		      self.display ( )  
		      prompt = "Input positions of 5 wolves like 11 21 32 44 52 with row index before the column index --> "
		      s = input ( prompt )
		      self.game (s )
		
		      prompt = "Play again (y/n) --> "
		      x = input ( prompt )
		      again = x == "y" or x == "Y"


x = wolves_and_sheep()
x.main()
