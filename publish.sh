#!/usr/bin/env bash
# This is a minimal integration script to publish our data and model from where we host the notebook, to our
# tutorial folder

cp -r data/ tutorial/
cp -r trained_models/ tutorial/
