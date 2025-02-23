import { Box, Text, Textarea } from "@chakra-ui/react";

interface Props {
  onTextChange: (text: string) => void;
}

const TextField = ({ onTextChange }: Props) => {
  return (
    <Box maxW="100%" as="fieldset" borderWidth="1px" p={4} borderRadius="md">
      <Text as="legend" fontWeight="bold" mb={2}>
        Enter your text:
      </Text>
      <Textarea
        placeholder="Type your text here..."
        size="lg"
        onChange={(e) => onTextChange(e.target.value)}
      />
    </Box>
  );
};

export default TextField;
