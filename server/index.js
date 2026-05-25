require('dotenv').config();

const app = require('./app');
const connectDB = require('./config/db');
const logger = require('./utils/logger');

const PORT = process.env.PORT || 4000;

const startServer = async () => {
  if (!process.env.MONGO_URI) {
    logger.error('MONGO_URI is not configured');
    process.exit(1);
  }

  await connectDB(process.env.MONGO_URI);

  app.listen(PORT, () => {
    logger.info(`EDMS API listening on port ${PORT}`);
  });
};

startServer();
