const dns = require('dns');
const mongoose = require('mongoose');
const logger = require('../utils/logger');

const connectDB = async (uri) => {
  try {
    const dnsServers = (process.env.MONGO_DNS_SERVERS || '')
      .split(',')
      .map((server) => server.trim())
      .filter(Boolean);

    if (dnsServers.length > 0) {
      dns.setServers(dnsServers);
      logger.info(`Using custom DNS servers for MongoDB: ${dnsServers.join(', ')}`);
    }

    await mongoose.connect(uri);
    logger.info('MongoDB connected');
  } catch (err) {
    logger.error(`MongoDB connection error: ${err.message}`);
    process.exit(1);
  }
};

module.exports = connectDB;
