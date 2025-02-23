import {
  ChakraProvider,
  Box,
  VStack,
  Button,
  Container,
  Flex,
} from "@chakra-ui/react";
import { defaultSystem } from "@chakra-ui/react";
import Header from "./components/Header";
import TextField from "./components/TextField";
import { useState } from "react";
import ModelSelector from "./components/ModelSelector";
import EntityList from "./components/EntityList";

function App() {
  const [text, setText] = useState<string>("");
  const [model, setModel] = useState<string>("spacy");
  const [entities, setEntities] = useState<Record<string, string>>({});

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    const response = await fetch("http://localhost:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, model }),
    });

    const data = await response.json();
    setEntities(data);
  };

  return (
    <ChakraProvider value={defaultSystem}>
      <Header />
      <Container maxW="container.md" centerContent>
        <Flex direction="column" w="100%" align="center" mt={8}>
          <Box maxW="100%" pt="100px" px={4}>
            <form onSubmit={handleSubmit}>
              <VStack align={"stretch"}>
                <ModelSelector model={model} setModel={setModel} />
                <TextField onTextChange={setText} />
                <Button
                  type="submit"
                  colorScheme="blue"
                  width="full"
                  color="blackAlpha.950"
                >
                  Process
                </Button>
              </VStack>
            </form>
            <EntityList entities={entities} />
          </Box>
        </Flex>
      </Container>
    </ChakraProvider>
  );
}

export default App;
