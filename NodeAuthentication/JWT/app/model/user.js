// get an instance of mongoose and mongoose.Schema

import mongoose from 'mongoose';
const Schema = mongoose.Schema;

// Set up a mongoose model and pass it using module.exports
module.exports = mongoose.model('User', new Schema({
    name: String,
    password: String,
    admin: Boolean
}));