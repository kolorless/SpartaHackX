import { StyleSheet, View, Text, TouchableOpacity, Image, SafeAreaView } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { useRouter } from 'expo-router';

export default function WorkoutScreen() {
  const router = useRouter(); // Hook at top level of component
  const username = "Yash";
  const workoutCount = 19;

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar style="dark" />
      
      {/* Top Logo */}
      <View style={styles.logoContainer}>
        <Text style={styles.logoText}>BOD FIX</Text>
      </View>

      {/* Main Content */}
      <View style={styles.content}>
        <Text style={styles.greeting}>Hey {username},</Text>
        <Text style={styles.workoutText}>
          You have recorded {workoutCount}{'\n'}workouts so far!
        </Text>
        
        <Text style={styles.subText}>Let's add another? 💪</Text>

        {/* Start Workout Button */}
        <TouchableOpacity style={styles.button} onPress={() => router.push("/(tabs)/camera")}>
          <Text style={styles.buttonText}>Start Workout</Text>
        </TouchableOpacity>

        {/* Barbell Image */}
        <View style={styles.barbellContainer}>
          {/* Replace with your actual barbell image */}
          <Image
            source={require('@/assets/images/barbell.png')}
            style={styles.barbellImage}
            resizeMode="contain"
          />
        </View>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFE4D6', // Peachy background color
  },
  logoContainer: {
    flexDirection: "row",
    height: 66.88,
    justifyContent: 'center',
    alignItems: 'center',
  },
  logoText: {
    fontSize: 36,
    fontWeight: 600,
    color: '#FF0000',
  },
  content: {
    flex: 1,
    paddingHorizontal: 20,
    paddingTop: 20,
  },
  greeting: {
    fontSize: 32,
    color: '#1E40AF', // Dark blue color
    fontWeight: '600',
    marginBottom: 10,
  },
  workoutText: {
    fontSize: 28,
    color: '#1E40AF',
    fontWeight: '500',
    lineHeight: 40,
    marginBottom: 20,
  },
  subText: {
    fontSize: 24,
    color: '#1E40AF',
    marginBottom: 30,
    marginTop: 40,
  },
  button: {
    backgroundColor: '#1E40AF',
    paddingVertical: 15,
    paddingHorizontal: 30,
    borderRadius: 8,
    alignSelf: 'flex-start',
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  buttonText: {
    color: '#FFF',
    fontSize: 20,
    fontWeight: '600',
  },
  barbellContainer: {
    position: 'absolute',
    padding: 0,
    bottom: 100,
    left: 0,
    right: 0,
    // alignItems: 'c',
  },
  barbellImage: {
    width: 200,
    height: 100,
  },
  navbar: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'center',
    paddingVertical: 20,
    borderTopWidth: 1,
    borderTopColor: 'rgba(0,0,0,0.1)',
    backgroundColor: '#FFD6C4', // Slightly darker shade for navbar
  },
  navItem: {
    padding: 10,
  },
  navCircle: {
    width: 24,
    height: 24,
    borderWidth: 2,
    borderColor: '#000',
    borderRadius: 12,
  },
  navHome: {
    width: 24,
    height: 24,
    borderWidth: 2,
    borderColor: '#000',
    transform: [{ rotate: '45deg' }],
  },
  navMenu: {
    width: 24,
    height: 18,
    justifyContent: 'space-between',
    alignItems: 'flex-end',
  },
});
