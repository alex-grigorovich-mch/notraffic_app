import React from "react";
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Button,
} from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import ControlButtons from "./Buttons";
import useIntersectionsStore from "../../store";

type Props = {
  handleOpen: () => void;
};

const MainTable: React.FC<Props> = ({ handleOpen }) => {
  const { intersections } = useIntersectionsStore();

  return (
    <TableContainer
      component={Paper}
      sx={{ maxWidth: 900, margin: "auto", overflow: "hidden" }}
    >
      <Table aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Intersection</TableCell>
            <TableCell align="right">Coordinate</TableCell>
            <TableCell align="right">Street 1</TableCell>
            <TableCell align="right">Street 2</TableCell>
            <TableCell align="right">
              <Button
                onClick={handleOpen}
                variant="contained"
                startIcon={<AddIcon />}
                size="small"
              >
                Add Intersection
              </Button>
            </TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {intersections.map(row => (
            <TableRow
              key={row.id}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.name}
              </TableCell>
              <TableCell align="right">
                {`${row.longitude}, ${row.latitude}`}
              </TableCell>
              <TableCell align="right">{row.first_street}</TableCell>
              <TableCell align="right">{row.second_street}</TableCell>

              <ControlButtons id={row.id} />
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default MainTable;
