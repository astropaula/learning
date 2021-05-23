import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import { Article, ArticleImage, Articles, Title, Wrapper } from 'components/SchoolNews/SchoolNews.styles';

const DATA_TOKEN= 'd0b07ea7c7d6f474f87a8dac0b2b50';
const query = `{
  allArticles {
    title
    content
    image {
      alt
      url
    }
  }
}`;

const SchoolNews = () => {
  const[articles, setArticles] = useState([]);
  useEffect(() => {
    fetch('https://graphql.datocms.com/', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${DATA_TOKEN}`,
      },
      body: JSON.stringify({
        query,
      })
    })
    .then(res => res.json())
    .then(({ data: { allArticles } }) => setArticles(allArticles))
    .catch(err => console.log(err));
  }, []);
  return (
    <Wrapper>
    <Title>Gazetka szkolna</Title>
    <Articles>
      {articles ? articles.map(article => (
        <Article>
          <ArticleImage>
            <img src={article.image.url} alt={article.image.alt} />
          </ArticleImage>
          <div>
            <h3>{article.title}</h3>
            <p>{article.content}</p>
          </div>
        </Article>
      )) : (
        <h2>no articles</h2>
      )}
    </Articles>
  </Wrapper>
  )
};

SchoolNews.propTypes = {};

export default SchoolNews;
