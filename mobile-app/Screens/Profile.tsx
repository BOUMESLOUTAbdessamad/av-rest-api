
import { Text, useColorScheme, SafeAreaView, View, StatusBar, ScrollView} from "react-native";

import {
    Colors} from 'react-native/Libraries/NewAppScreen';
  
function Profile():JSX.Element {

    const isDarkMode = useColorScheme() === 'dark';

    const backgroundStyle = {
      backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,
    };

    const textStyle = {
        color: isDarkMode ? Colors.lighter : Colors.darker,
      };
    return (
    <SafeAreaView style={backgroundStyle}>
      <StatusBar
        barStyle={isDarkMode ? 'light-content' : 'dark-content'}
        backgroundColor={backgroundStyle.backgroundColor}
      />
         <ScrollView
        contentInsetAdjustmentBehavior="automatic"
        style={backgroundStyle}>
        <View style={{height: 1000}}>
            <Text style={textStyle}>
                Profile View
            </Text>
        </View>
        </ScrollView>
       </SafeAreaView>
    )
}

export default Profile;