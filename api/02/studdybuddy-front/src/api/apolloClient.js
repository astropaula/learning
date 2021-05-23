import { ApolloClient, createHttpLink, InMemoryCache } from '@apollo/client';
import { setContext } from '@apollo/client/link/context';

const DATA_TOKEN= 'd0b07ea7c7d6f474f87a8dac0b2b50';

const httpLink = createHttpLink({
    uri: 'https://graphql.datocms.com/'
});

const authLink = setContext((_, { headers }) => {
    return {
        headers: {
            ...headers,
            authorization: `Bearer ${DATA_TOKEN}`,
        }
    }
});

export const apolloClient = new ApolloClient({
    link: authLink.concat(httpLink),
    cache: new InMemoryCache(),
});