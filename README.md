# PyData Carolinas 2016 Tutorial: Datascience on the web

Welcome to Datascience on the web, with Don and Francois.

You have been given a paper with a URL in the form: https://xxxxx-xxx.dionresearch.com:8088

Point your browser to it and type the accompanying password.

Problems? Raise your hand and somebody will help you, even perhaps your neighbor. Also, feel free to tweet about this
 session. I am @f_dion and this is #datascience and #flask at #pydatacarolinas.

# After the fact

The unrefactored notebook is [here](https://github.com/fdion/pydata/blob/master/notebooks/PyData.ipynb) while the refactored one is [here](https://github.com/fdion/pydata/blob/master/notebooks/PyData-Refactored.ipynb).

Once you run through the whole refactored notebook, you will have train and test sets saved in data/ and a trained 
model in trained_models/. To make these available in the tutorial directory, you will have to run the publish.sh 
script. On a unix like environment (mac, linux etc):

    chmod a+x publish.sh
    ./publish.sh

# Video

The whole session is now on youtube: [Francois Dion & Don Jennings Datascience on the web](https://www.youtube.com/watch?v=qP_8ch-5XhE)

# Updates

This repository will get a few more files after the tutorial, including some PDFs. Make sure you watch the repo if you want the latest information.

# The basics

- [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
- [HTML tutorials and reference](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [Flask](http://flask.pocoo.org/)
- [Jinja2 template designer docs](http://jinja.pocoo.org/docs/dev/templates/)

# The Machine Learning

 - [Linear Models in Scikit-learn](http://scikit-learn.org/stable/modules/linear_model.html)
 - [Cross validation](http://scikit-learn.org/stable/modules/cross_validation.html)
 - [RFE](http://scikit-learn.org/stable/modules/feature_selection.html#rfe)
 - [Model persistence](http://scikit-learn.org/stable/modules/model_persistence.html)

# The visualization

 - [Matplotlib](http://matplotlib.org/)
 - [Seaborn](https://github.com/mwaskom/seaborn)
 - [Stemgraphic](https://github.com/fdion/stemgraphic)
 - [MPLD3](http://mpld3.github.io/)
 
 Other options for jupyter and flask compatible visualizations:
 - [plot.ly](http://plot.ly)
 - [Bokeh](http://bokeh.pydata.org/en/latest/)
 - [Pygal](http://www.pygal.org/en/stable/)
 - [Altair](https://pypi.python.org/pypi/altair/1.0.0)

# Further reading

Check out these awesome lists:
 - [The list of lists](https://github.com/sindresorhus/awesome)
 - [The awesome flask list](https://github.com/humiaozuzu/awesome-flask)
 
 And this video for building APIs with [flask-restplus](http://flask-restplus.readthedocs.io/en/stable/): [you-tube video](https://www.youtube.com/watch?v=hV2ccg4mw_Q&feature=youtu.be)

# Automating the basics

 - [Cookiecutter](https://github.com/audreyr/cookiecutter)
 - [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask) : A Flask template with Bootstrap 3, starter templates, and working user registration.
 - [cookiecutter-flask-2](https://github.com/wdm0006/cookiecutter-flask): A heavier weight fork of cookiecutter-flask, with more boilerplate including forgotten password and Heroku integration
 - [cookiecutter-flask-foundation](https://github.com/JackStouffer/cookiecutter-Flask-Foundation) : Flask Template with caching, forms, sqlalchemy and unit-testing.
