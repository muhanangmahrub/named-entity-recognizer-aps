import { Box, Heading, List } from "@chakra-ui/react";

interface Props {
  entities: Record<string, string>;
}

const EntityList = ({ entities }: Props) => {
  return (
    <Box mt={6} p={4} borderWidth={1} borderRadius="md">
      <Heading size="md" mb={2}>
        Entities
      </Heading>
      <List.Root>
        {Object.entries(entities).map(([word, entity]) => (
          <List.Item key={word}>
            <strong>{word}</strong>: {entity}
          </List.Item>
        ))}
      </List.Root>
    </Box>
  );
};

export default EntityList;
