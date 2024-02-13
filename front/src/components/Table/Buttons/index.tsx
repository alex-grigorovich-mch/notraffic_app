import { TableCell, IconButton } from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";
import useIntersectionsStore from "../../../store";
import MainModal from "../../Modal";
import { useState } from "react";

type Props = {
  id: number;
};

const ControlButtons: React.FC<Props> = ({ id }) => {
  const { intersections, removeIntersection, updateIntersection } =
    useIntersectionsStore();

  const selectedIntersection = intersections.filter(item => item.id == id);

  const [formData, setFormData] = useState({
    name: selectedIntersection[0]?.name || "",
    longitude: selectedIntersection[0]?.longitude || "",
    latitude: selectedIntersection[0]?.latitude || "",
    first_street: selectedIntersection[0]?.first_street || "",
    second_street: selectedIntersection[0]?.second_street || "",
  });

  const [modalOpen, setModalOpen] = useState(false);
  const handleClose = () => setModalOpen(false);

  const handleChange = (event: { target: { name: string; value: string } }) => {
    const { name, value } = event.target;
    setFormData(prevFormData => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  const handleModalSubmit = () => {
    updateIntersection(
      id,
      formData.name,
      formData.longitude,
      formData.latitude,
      formData.first_street,
      formData.second_street,
    );
    handleClose();

    console.log("working");
  };

  return (
    <>
      <TableCell align="right">
        <IconButton
          aria-label="edit"
          size="small"
          onClick={() => setModalOpen(true)}
        >
          <EditIcon fontSize="inherit" />
        </IconButton>
        <IconButton
          aria-label="delete"
          size="small"
          onClick={() => removeIntersection(id)}
        >
          <DeleteIcon fontSize="inherit" />
        </IconButton>
      </TableCell>
      <MainModal
        modalOpen={modalOpen}
        handleClose={handleClose}
        handleChange={handleChange}
        formData={formData}
        handleModalSubmit={handleModalSubmit}
      />
    </>
  );
};

export default ControlButtons;
