// src/hooks/useUserSearch.js
import { useState, useMemo } from 'react';

export const useUserSearch = (initialUsers) => {
  const [users, setUsers] = useState(initialUsers);
  const [searchTerm, setSearchTerm] = useState("");
  const [roleFilter, setRoleFilter] = useState("All");
  const [statusFilter, setStatusFilter] = useState("All");

  // Toggle Status Logic
  const toggleUserStatus = (id) => {
    setUsers((prevUsers) =>
      prevUsers.map((user) =>
        user.id === id ? { ...user, active: !user.active } : user
      )
    );
  };

  // Filtering Logic
  const filteredUsers = useMemo(() => {
    return users.filter((user) => {
      // 1. Search (Case insensitive + trim)
      const matchesSearch = user.name
        .toLowerCase()
        .includes(searchTerm.trim().toLowerCase());

      // 2. Role Filter
      const matchesRole = roleFilter === "All" || user.role === roleFilter;

      // 3. Status Filter
      const userStatus = user.active ? "Active" : "Inactive";
      const matchesStatus = statusFilter === "All" || userStatus === statusFilter;

      return matchesSearch && matchesRole && matchesStatus;
    });
  }, [users, searchTerm, roleFilter, statusFilter]);

  return {
    users,
    filteredUsers,
    searchTerm,
    setSearchTerm,
    roleFilter,
    setRoleFilter,
    statusFilter,
    setStatusFilter,
    toggleUserStatus,
  };
};