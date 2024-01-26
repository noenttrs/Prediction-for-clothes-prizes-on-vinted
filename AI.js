const tf = require('@tensorflow/tfjs')
const sk = require('scikitjs')
const xslx = require('node-xlsx')

sk.setBackend(tf)

const file = xslx.parse('Clothes_filtered.xlsx')


