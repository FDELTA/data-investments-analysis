def price_distribution(df, x):
	'''
	Esta función esta diseñada para recibir uno de los cinco barrios de NY y te devuelve su distribución por precios
	'''
	import seaborn as sns
	import matplotlib.pyplot as plt
	print('Please select the neighbourhodod: ')
	x=input()
	df1 = df[df.neighbourhood_group == x][["neighbourhood","price"]]
	d = df1.groupby("neighbourhood").mean()
	sns.distplot(d)
	return plt.show()
def data_zone(df, x, y):
	'''
	Esta función esta diseñada para recibir o bien price o bien avialablity_365 y retornar un gráfico térmico
	'''
	import seaborn as sns
	import matplotlib.pyplot as plt
	card = df[df[x]< y]
	card.plot(kind='scatter', x='longitude', y='latitude',c=x, cmap=plt.get_cmap('jet'), colorbar=True, alpha=0.4)


def pie_chart_price_availability(df, x):
	'''
	Esta función esta diseñada para recibir o bien price o bien availability_365 y devolver el porcentaje en sus rangos
	'''
	import seaborn as sns
	import matplotlib.pyplot as plt
	a = df[df[x]<=90].count()[0]
	b = df[(df[x]>90) & (df[x]<=180)].count()[0]
	c = df[(df[x]>180) & (df[x]<=270)].count()[0]
	d = df[(df[x]>270)].count()[0]
	labels = 'Less than 90','Between 90 & 180','Between 180 & 270','Greater than 270'
	sizes = a,b,c,d
	explode = (.1,.1,.1,.1)
	availability_pie = plt.pie(sizes,labels=labels,explode=explode,shadow=True,startangle=90,autopct='%1.1f%%',radius=1.1)
	plt.title('Calendar Year 2019')

def plot_bar(df,y):
	'''
	Esta función recibe un DataFrame y devuelve un plot bar al que puedes nombrar tanto los ejes como el título
	'''
	import seaborn as sns
	import matplotlib.pyplot as plt
	plt.bar(x=y.index, height=y, alpha=.7)
	print('Enter the title of the chart: ')
	z= input()
	print('Enter the ylabel: ')
	n= input()
	print('Enter the xlabel: ')
	h= input()
	plt.title(z, color='red', fontsize=15)
	plt.ylabel(n, color='blue', fontsize=13)
	plt.xlabel(h,color='blue', fontsize=13)


