import React, {useState, useCallback, useEffect} from 'react';

import {
  useColorScheme,
  SafeAreaView,
  View,
  StatusBar,
  ScrollView,
  StyleSheet,
} from 'react-native';
import {Avatar, Button, Card, Searchbar, Text} from 'react-native-paper';
import {Colors} from 'react-native/Libraries/NewAppScreen';

import axios from 'axios';
// const axios = require('axios')

function Home(): JSX.Element {
  const isDarkMode = useColorScheme() === 'dark';
  const backgroundStyle = {
    backgroundColor: isDarkMode ? Colors.darker : '#FFFFFF',
  };
  const textStyle = {
    color: isDarkMode ? Colors.lighter : Colors.darker,
  };

  const [keywords, setKeywords] = useState('');
  const [hikes, setHikes] = useState([]);
  const [loading, setLoading] = useState(false);

//   const axiosInstance = axios.create({baseURL: 'http://127.0.0.1:5000'});

  useEffect(() => {
    // if (keywords != '') {

    setLoading(true);
    const fetchHikes = async () => {
      await axios

        .get('http://127.0.0.1:5000/api/v0/hikes') // GET /api/v0/hikes
        .then(res => {

          setHikes(res.data);
          // setLoading(false);
          return;
        })
        .catch(error => console.log(error));
    };
    fetchHikes();
    console.log(hikes);
    // }
  });


  return (
    <SafeAreaView style={backgroundStyle}>
      <StatusBar
        barStyle={isDarkMode ? 'light-content' : 'dark-content'}
        backgroundColor={backgroundStyle.backgroundColor}
      />
      <ScrollView
        scrollEnabled={true}
        contentInsetAdjustmentBehavior="automatic"
        style={backgroundStyle}>
        <View style={{backgroundColor: '#FFFFFF', height: 1000}}>
          <View style={{padding: 10}}>
            <Searchbar
              style={{borderRadius: 30, backgroundColor: '#FFFFFF'}}
              elevation={5}
              placeholder="Search"
              inputStyle={{fontSize: 18, fontWeight: '200'}}
              iconColor="#222222"
              onChangeText={keywords => setKeywords(keywords)}
              value={keywords}
              onSubmitEditing={() => {
                if (keywords.trim() != '' || !keywords.trim())
                  alert('Search : ' + keywords.trim());
                else alert('Empty value');
              }}
            />
          </View>
          <View style={{padding: 10}}>
            <Text style={[textStyle, {fontSize: 32, fontWeight: '700'}]}>
              Popular Products
            </Text>
          </View>
          <View style={{marginVertical: 10, height: '100%'}}>
            <ScrollView horizontal={true}>
              <Card style={styles.Card} elevation={6}>
                <Card.Cover
                  source={{uri: 'https://picsum.photos/700'}}
                  style={{borderRadius: 30}}
                />
                <Card.Content style={styles.CardContent}>
                  <Text variant="titleLarge">Oran</Text>
                </Card.Content>
              </Card>
              <Card style={styles.Card} elevation={6}>
                <Card.Cover
                  source={{uri: 'https://picsum.photos/700'}}
                  style={{borderRadius: 30}}
                />
                <Card.Content style={styles.CardContent}>
                  <Text variant="titleLarge">Jijel</Text>
                </Card.Content>
              </Card>
              <Card style={styles.Card} elevation={6}>
                <Card.Cover
                  source={{uri: 'https://picsum.photos/700'}}
                  style={{borderRadius: 30}}
                />
                <Card.Content style={styles.CardContent}>
                  <Text variant="titleLarge">Annaba</Text>
                </Card.Content>
              </Card>
            </ScrollView>
          </View>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

export default Home;

const styles = StyleSheet.create({
  Card: {
    margin: 10,
    padding: 2,
    // paddingHorizontal:2,
    // paddingVertical: 10,
    width: 300,
    maxHeight: 270,
    backgroundColor: '#FFFFFF',
    borderRadius: 32,
    // maxHeight:
  },
  CardContent: {
    marginVertical: 8,
  },
  sectionContainer: {
    marginTop: 32,
    paddingHorizontal: 24,
  },
  sectionTitle: {
    fontSize: 24,
    fontWeight: '600',
  },
  sectionDescription: {
    marginTop: 8,
    fontSize: 18,
    fontWeight: '400',
  },
  highlight: {
    fontWeight: '700',
  },
});
