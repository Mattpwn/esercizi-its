
import { useState } from 'react';
import { Button, FlatList, StyleSheet, Text, TextInput, View, Modal, ScrollView, Image } from 'react-native';
import TaskItem from './components/TaskItem';

export default function App() {
  const [tasks, setTasks] = useState([])
  const [task, setTask] = useState("")
  function taskInputHandler(enteredTask){
    console.log(enteredTask);
    setTask(enteredTask)
  }

  function addTaskHandler(){
    if (task !== ""){
    setTasks(current =>[...current,{task, id:new Date()}]);
    setTask("")
    }
  }
  return (
    <View style={styles.appContainer}>
      <View  style={styles.inputContainer}>
        <TextInput 
        style ={styles.textInput} 
        placeholder = "Inserisci task" 
        onChangeText={taskInputHandler}
        value = {task}
        
        />
     <Button 
     
     title = "Aggiungimi"
     onPress = {addTaskHandler}
     disabled = {task === ""}
     ></Button>
    </View>
    <View style={styles.goalsContainer}>

      <FlatList alwaysBounceVertical = {false}
      data = {tasks}
      renderItem = {(itemData) => {
        return (
          <TaskItem taskItem={itemData.item}></TaskItem>
          // <View style = {styles.taskItem}>
          //   <Text style = {styles.taskText} >{itemData.item}</Text>
          // </View>
        
        );
      }}
      keyExtractor={(item) => item.id}
      />
    {/* //   <ScrollView>
    //   {
    //     tasks.map((t,index) => (
    //       <View key={index} style = {styles.taskItem} >
    //       <Text style = {styles.taskText} > {t}</Text>
    //       </View>
    //     ))
    //   }
    // </ScrollView> */}
    </View>

    {/* <View style={{ flexDirection: 'row', height: 200}}>
      <View style={{ backgroundColor: 'red', flex:1 }} />
      <View style={{ backgroundColor: 'white', flex:1 }} />
      <View style={{ backgroundColor: 'green', flex: 1}} />
    </View>
    <View>
        <Image></Image>
    </View> */}

    </View> 
  );
}

const styles = StyleSheet.create({ // fornisce auto completamento 
  appContainer: {
    flex: 1,
    backgroundColor: 'skyblue',
    paddingTop:50,
    paddingHorizontal:16,
    
  },
  inputContainer:{
    flex:1,
    flexDirection:'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingBottom: 24,
    borderBottomWidth: 3,
    borderColor: 'purple',

    
  },
  textInput:{
    borderWidth: 3,
    borderColor: 'purple',
    width:'70%',
    padding: 8,
  },
  goalsContainer:{
    flex:4,
   

  },
  taskItem: {
    margin: 8,
    padding: 8,
    borderRadius: 6,
    color: "#fff",
    backgroundColor: '#5e0acc'
  },
  taskText: {
    color: '#cccccc'
  }
  
 
});

