import { StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import { Button, FlatList, StyleSheet, Text, TextInput, View, Modal } from 'react-native';

export default function App() {
  const [messaggio, setMessaggio] = useState("Ciao");
  const [visible, setVisible] = useState(false);
  const [nome, setNome] = useState("");
  const [openModal, setOpenModal] = useState(false);
  const [contatore, setContatore] = useState(0);
  const [a, setA] = useState("");
  const [b, setB] = useState("");

  const somma = Number (a) + Number (b);

  const dati=[
    {id:"1", nome:"Camilla"},
    {id:"2", nome:"Matteo"},
    {id:"3", nome:"Luchetto"}
  ]
  return (
    <View style={styles.container}>
      <Text>{nome}</Text>
      {visible && <Text>{messaggio} {visible}</Text>}
      <TextInput placeholder = "Inserisci testo" onChangeText = {setNome} style = {styles.inputText}></TextInput>
      <Button title = 'Cambia testo' onPress = {() => setMessaggio("Ho premuto il pulsante")}/>
      <Button title = {visible ? "Nascondi" : "Visualizza"} onPress = {() => setVisible(!visible)} />
        <Text>{contatore}</Text>
        <Button title='Incrementa' onPress={()=>setContatore(current => current +1)}></Button>
        <Button title='Decrementa' onPress={()=>setContatore(current => current -1)}></Button>
        <Button title='Azzera' onPress={()=>setContatore(0)}></Button>
        <TextInput
          placeholder='Inserisci un numero'
          onChangeText={setA}
          style = {styles.inputText}
        />
        <TextInput
          placeholder='Inserisci un numero'
          onChangeText={setB}
          style = {styles.inputText}
        />
        <Text> {somma}</Text>

      <View style = {styles.containerList}>
      <FlatList
      data = {dati}
      renderItem={(dato) => <Text>{dato.item.nome}</Text>}
      keyExtractor={(item) => item.id}
      />
      </View>
      <View style={styles.containerList}>
        <Text>Bella rega</Text>
        <Button title='Apri' onPress={() => setOpenModal(true)}></Button>
        <Modal visible={openModal} animationType='slide'>
          <View>
            <Text>non vedo l'ora di andare a casa</Text>
            <Button title='Chiudi' onPress={() => setOpenModal(false)}></Button>
          </View>
        </Modal>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'skyblue',
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal:46,
    padding:50
  },
  containerList:{
    flex: 3,
    backgroundColor: "skyblue",
    alignItems: "center",
    justifyContent: "center",
  },
  inputText:{
    borderWidth: 1,
    padding: 10
  }
});