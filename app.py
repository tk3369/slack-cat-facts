#!/usr/bin/env python3

from aws_cdk import core

from cat_facts.cat_facts_stack import CatFactsStack


app = core.App()
CatFactsStack(app, "cat-facts")

app.synth()
