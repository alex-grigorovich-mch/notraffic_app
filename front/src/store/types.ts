export type Intersection = {
  id: number;
  name: string;
  longitude: string;
  latitude: string;
  first_street: string;
  second_street: string;
};

export type AddIntersection = (
  name: string,
  longitude: string,
  latitude: string,
  first_street: string,
  second_street: string,
) => void;

export type RemoveIntersection = (id: number) => void;

export type UpdateIntersection = (
  id: number,
  name: string,
  longitude: string,
  latitude: string,
  first_street: string,
  second_street: string,
) => void;

export type IntersectionStore = {
  intersections: Intersection[];
  error: { status?: number; message: string } | null;
  fetchIntersections: () => void;
  addIntersection: AddIntersection;
  removeIntersection: RemoveIntersection;
  updateIntersection: UpdateIntersection;
};
