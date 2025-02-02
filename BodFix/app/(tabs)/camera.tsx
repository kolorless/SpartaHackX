import { CameraView, CameraType, useCameraPermissions } from 'expo-camera';
import { useRef, useState } from 'react';
import { Button, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { IconSymbol } from '@/components/ui/IconSymbol';

export default function App() {
  const [facing, setFacing] = useState<CameraType>('back');
  const cameraRef = useRef<CameraView>(null);
  const [permission, requestPermission] = useCameraPermissions();
  const [isRecording, setRecording] = useState<boolean>(false);

  if (!permission) {
    // Camera permissions are still loading.
    return <View />;
  }

  if (!permission.granted) {
    // Camera permissions are not granted yet.
    return (
      <View style={styles.container}>
        <Text style={styles.message}>We need your permission to show the camera</Text>
        <Button onPress={requestPermission} title="Grant permission" />
      </View>
    );
  }

  async function startRecording() {
    console.log("Recording started")
    setRecording(true);
    let prom =  cameraRef.current?.recordAsync().then((uri) => {
        console.log("Recorded", uri);
    })
  }

  async function stopRecording() { 
    console.log("Stop recording");
    setRecording(false);
    cameraRef.current?.stopRecording();
  }

  return (
    <View style={styles.container}>
      <CameraView mode = 'video' ref = {cameraRef} style={styles.camera} facing={facing}>
        <View style={styles.buttonContainer}>
          <TouchableOpacity style={!isRecording? styles.start_button : styles.stop_button} onPress={!isRecording?startRecording:stopRecording }>
            <Text style={!isRecording? styles.start_text : styles.stop_text}>{!isRecording? "Start Recording" : "Stop Recording"  }</Text>
          </TouchableOpacity>
        </View>
      </CameraView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
  },
  message: {
    textAlign: 'center',
    paddingBottom: 10,
  },
  camera: {
    flex: 1,
  },
  buttonContainer: {
    flex: 1,
    flexDirection: 'row',
    backgroundColor: 'transparent',
    margin: 64,
  },
  start_button: {
    flex: 1,
    alignSelf: 'flex-end',
    alignItems: 'center',
    backgroundColor: 'red',
    marginBottom: "64",
    padding: 10,
    borderRadius: 30,
  },
  stop_button: {
    flex: 1,
    alignSelf: 'flex-end',
    alignItems: 'center',
    backgroundColor: 'white',
    marginBottom: "64",
    padding: "10",
    borderRadius: 30,
  },
  start_text: {
    fontSize: 18,
    fontWeight: 'bold',
    color: 'white',
  },
  stop_text: {
    fontSize: 18,
    fontWeight: 'bold',
    color: 'red',
  },
});
