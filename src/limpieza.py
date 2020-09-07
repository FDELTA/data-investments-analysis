def clean_header(df):
	"""
	Esta función elimina caracteres no deseados y espacios de los nombres de las columnas, mientras conserva todo en minúscula
	"""
	df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
	return df.columns

