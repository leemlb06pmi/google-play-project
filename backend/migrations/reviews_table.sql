DROP TABLE IF EXISTS app_reviews;

CREATE TABLE IF NOT EXISTS app_reviews (
  id serial PRIMARY KEY,
  app VARCHAR(255),
  translated_review TEXT,
  sentiment VARCHAR(255),
  sentiment_polarity DECIMAL,
  sentiment_subjectivity DECIMAL
); 