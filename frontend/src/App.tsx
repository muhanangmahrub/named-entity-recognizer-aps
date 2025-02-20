import { ChakraProvider } from "@chakra-ui/react";
import { defaultSystem } from "@chakra-ui/react";
import Header from "./components/Header";
import TextField from "./components/Body";

function App() {
  return (
    <ChakraProvider value={defaultSystem}>
      <Header />
      <TextField />
    </ChakraProvider>
  );
}

export default App;
