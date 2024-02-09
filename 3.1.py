movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"git add .
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def first(single_movie):
    for movie in movies:
        imdb_rating = movie["imdb"]
        if imdb_rating > 5.5:
            return True
        else:
            return False

single_movie = input("1. Enter a movie")
res = first(single_movie)
print(res)

def second(movies):
    sublst = []
    for movie in movies:
        imdb_rating = movie["imdb"]
        if imdb_rating > 5.8:
            sublst.append(movie["name"])
    return sublst


res2 = second(movies)
print(f"2.  {res2}")

def third(category_inp):
    sublst = []
    for movie in movies:
        imdb_cat = movie["category"]
        if imdb_cat == category_inp:
            sublst.append(movie["name"])
    return sublst

category_inp = input("3.Enter category: ")
res3 = third(category_inp)
print(res3)

def fourth(lsp):
    x = 0
    t = 0
    for movie in lsp:
        for mov in movies:
            if movie == mov["name"]:
                x+=mov["imdb"]
                t+=1
                break
    resu = x/t
    return resu

lsp = ["Dark Knight", "The Help", "Hitman"]
res4 = fourth(lsp)
print(f"this the avg of sum movies - {res4}")

def fifth(cat_nam):
    x = 0
    t = 0
    for mov in movies:
        if cat_nam == mov["category"]:
            x+=mov["imdb"]
            t+=1
            break
    resu = x/t
    return resu

cat_nam = input("5.Enter a category: ")
res5 = fifth(cat_nam)
print(res5)

