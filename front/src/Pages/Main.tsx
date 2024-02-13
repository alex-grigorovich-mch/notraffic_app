import { useEffect, useState } from "react";
import MainModal from "../components/Modal";
import MainTable from "../components/Table";
import useIntersectionsStore from "../store";
import ErrorModal from "../components/ErrorModal";


const initialFormState = {
  name: "",
  longitude: "",
  latitude: "",
  first_street: "",
  second_street: "",
};


function Main() {
  const [isErrorModalOpen, setIsErrorModalOpen] = useState(false);
  const [modalOpen, setModalOpen] = useState(false);
  const [formData, setFormData] = useState(initialFormState);

  const handleOpen = () => setModalOpen(true);
  const handleClose = () => setModalOpen(false);

  const handleChange = (event: { target: { name: string; value: string } }) => {
    const { name, value } = event.target;
    setFormData(prevFormData => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  const { addIntersection, fetchIntersections, error } = useIntersectionsStore();

  useEffect(() => {
    fetchIntersections();
  }, [fetchIntersections]);

  const handleModalSubmit = () => {
    addIntersection(
      formData.name,
      formData.longitude,
      formData.latitude,
      formData.first_street,
      formData.second_street,
    );
    setModalOpen(false);
    setFormData(initialFormState);
  };

  useEffect(() => {
    if (error) {
      setIsErrorModalOpen(true);
    } else {
      setIsErrorModalOpen(false);
    }
  }, [error]);

  return (
    <div style={{ padding: 16 }}>
      <MainTable handleOpen={handleOpen} />

      <MainModal
        modalOpen={modalOpen}
        handleClose={handleClose}
        handleChange={handleChange}
        formData={formData}
        handleModalSubmit={handleModalSubmit}
      />
      <ErrorModal
        isErrorModalOpen={isErrorModalOpen}
        setIsErrorModalOpen={setIsErrorModalOpen}
      />
    </div>
  );
}

export default Main;
