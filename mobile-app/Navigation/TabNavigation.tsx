import React , { useState, useCallback } from 'react';

import { createMaterialBottomTabNavigator } from '@react-navigation/material-bottom-tabs';
import Icon from 'react-native-vector-icons/FontAwesome';

import Home  from "../Screens/Home";
import Notifications  from "../Screens/Notifications";
import Profile  from "../Screens/Profile";
import BookMarks  from "../Screens/BookMarks";

const Tab = createMaterialBottomTabNavigator();

function TabNavigation() {



  return (
    <Tab.Navigator
        // activeColor="#3e0000"
        // inactiveColor="#3e2465"
        barStyle={{ backgroundColor: '#FFFFFF'}}
        style={{borderRadius:25}}
        
    >

      <Tab.Screen name="Home" component={Home}
          
          options={{
            tabBarIcon: ({ color }) => (
              <Icon name="home" size={24}/>
            ),
          }}
      
      />
      <Tab.Screen name="BookMarks" component={BookMarks}
          options={{
            tabBarIcon: ({ color }) => (
              <Icon name="bookmark" size={24}/>
            ),
          }}
       />
      <Tab.Screen name="Notifications" component={Notifications} 
      options={{ 
        tabBarIcon: ({ color }) => (
              <Icon name="bell" size={24}/>
            ), tabBarBadge: 1 
            }} 
            />
      <Tab.Screen name="My Profile" component={Profile} 
          options={{ 
            tabBarIcon: ({ color }) => (
                <Icon name="user" size={24}/>
              )
              }} 
      />
    </Tab.Navigator>
  );
}

export default TabNavigation;