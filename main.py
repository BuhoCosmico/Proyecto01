from fastapi import FastAPI
import pandas as pd
from starlette.responses import RedirectResponse

amazon = pd.read_csv("amazon_limpio.csv")
disney = pd.read_csv("disney_limpio.csv")
hulu = pd.read_csv("hulu_limpio.csv")
netflix = pd.read_csv("netflix_limpio.csv")
new_dataset = pd.read_csv("new_dataset_limpio.csv")



app = FastAPI(title = 'Proyecto_01', 
              description = 'ETL y consulta a los Datasets', 
              version = '1.0.1')

@app.get("/")
async def read_root():
    return RedirectResponse(url="/docs/")

@app.get('/ejercicio1/{platform}/{palabra}')
async def get_word_count(platform:str, palabra:str):
    cont = 0

    if platform == 'netflix':
        for i,e in enumerate(netflix['title']):
            if (palabra in e):
                cont+=1

    if platform == 'disney':
        for i,e in enumerate(disney['title']):
            if (palabra in e):
                cont+=1

    if platform == 'hulu':
        for i,e in enumerate(hulu['title']):
            if (palabra in e):
                cont+=1

    if platform == 'amazon':
        for i,e in enumerate(hulu['title']):
            if (palabra in e):
                cont+=1

    return('platform: '+str(platform)+
            '       cantidad: '+str(cont))


@app.get('/ejercicio2/{plataforma}/{score}/{year}')
async def get_score_count(plataforma:str, score:int, year:int):

    if plataforma == 'disney':
        d = disney[(disney['score'] > score) & (disney['release_year'] == year) & (disney['type'] == 'movie')]
        dis = len(d)
        return('platform: '+str(plataforma)+
                '       cantidad: '+str(dis))

    if plataforma == 'netflix':
        n = netflix[(netflix['score'] > score) & (netflix['release_year'] == year) & (netflix['type'] == 'movie')] 
        net = len(n)
        return('platform: '+str(plataforma)+
                '       cantidad: '+str(net))

    if plataforma == 'hulu':
        h = hulu[(hulu['score'] > score) & (hulu['release_year'] == year) & (hulu['type'] == 'movie')]
        hul = len(h)
        return('platform: '+str(plataforma)+
                '       cantidad: '+str(hul))

    if plataforma == 'amazon':
        a = amazon[(amazon['score'] > score) & (amazon['release_year'] == year) & (amazon['type'] == 'movie')]
        amzn = len(a)
        return('platform: '+str(plataforma)+
                '       cantidad: '+str(amzn))


@app.get('/ejercicio3/{plataforma}')
async def get_second_score(plataforma:str):

    if plataforma == 'amazon':
        df = amazon[(amazon['type'] == 'movie') & (amazon['score'] == amazon['score'].max())]
        scor = df['score'].iloc[0]
        df = df['title'].sort_values(ascending = True)
        d = df.iloc[1]
        return(' title: ' +str(d)+
                '    score: '+ str(scor))

    if plataforma == 'netflix':
        df = netflix[(netflix['type'] == 'movie') & (netflix['score'] == netflix['score'].max())]
        scor = df['score'].iloc[0]
        df = df['title'].sort_values(ascending = True)
        d = df.iloc[1]
        return(' title: ' +str(d)+
                '    score: '+ str(scor))

    if plataforma == 'hulu':
        df = hulu[(hulu['type'] == 'movie') & (hulu['score'] == hulu['score'].max())]
        scor = df['score'].iloc[0]
        df = df['title'].sort_values(ascending = True)
        d = df.iloc[1]
        return(' title: ' +str(d)+
                '    score: '+ str(scor))

    if plataforma == 'disney':
        df = disney[(disney['type'] == 'movie') & (disney['score'] == disney['score'].max())]
        scor = df['score'].iloc[0]
        df = df['title'].sort_values(ascending = True)
        d = df.iloc[1]
        return(' title: ' +str(d)+
                '    score: '+ str(scor))

@app.get('/ejercicio4/{title}/{duration}/{year}')
async def get_longest(title:str, duration:str, year:int):

    if title == 'netflix':
        df = netflix[(netflix['release_year'] == year) & (netflix['duration_type'] == duration)]
        g = df['duration_int'].max()
        f = df.loc[df.duration_int.idxmax()]['title']
        return('title: ' + str(f) +
                '     duration: ' + str(g) +
                '     duration_type: ' + str(duration))

    if title == 'amazon':
        df = amazon[(amazon['release_year'] == year) & (amazon['duration_type'] == duration)]
        g = df['duration_int'].max()
        f = df.loc[df.duration_int.idxmax()]['title']
        return('title: ' +str(f)+
                '     duration: ' +str(g)+
                '     duration_type: ' +str(duration))

    if title == 'disney':
        df = netflix[(netflix['release_year'] == year) & (netflix['duration_type'] == duration)]
        g = df['duration_int'].max()
        f = df.loc[df.duration_int.idxmax()]['title']
        return('title: ' + str(f) +
                '     duration: ' + str(g) +
                '     duration_type: ' + str(duration))

    if title == 'hulu':
        df = netflix[(netflix['release_year'] == year) & (netflix['duration_type'] == duration)]
        g = df['duration_int'].max()
        f = df.loc[df.duration_int.idxmax()]['title']
        return('title: ' + str(f) +
                '     duration: ' + str(g) +
                '     duration_type: ' + str(duration))

@app.get('/ejercicio5/{num}')
async def get_rating_count(num:str):

    df = new_dataset[new_dataset['rating'] == num]
    dff = len(df['title'])
    return ('rating: '+ str(num)+ 
            '      cantidad: '+ str(dff))
