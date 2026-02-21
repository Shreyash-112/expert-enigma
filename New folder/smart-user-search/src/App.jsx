// src/App.jsx
import React from 'react';
import { useUserSearch } from './hooks/useUserSearch';
import './index.css'; // We will style it in the next step

const USERS = [
  { id: 1, name: "Aman Gupta", role: "Admin", active: true },
  { id: 2, name: "Rahul Sharma", role: "User", active: false },
  { id: 3, name: "Ankit Verma", role: "User", active: true },
  { id: 4, name: "Neha Singh", role: "Admin", active: true },
  { id: 5, name: "Riya Patel", role: "User", active: false },
];

function App() {
  const {
    users,
    filteredUsers,
    searchTerm,
    setSearchTerm,
    roleFilter,
    setRoleFilter,
    statusFilter,
    setStatusFilter,
    toggleUserStatus
  } = useUserSearch(USERS);

  return (
    <div className="container">
      <h1 className="title">Smart User Search</h1>

      {/* Controls Section */}
      <div className="controls">
        <input
          type="text"
          placeholder="Search by name..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="search-input"
        />
        
        <select 
          value={roleFilter} 
          onChange={(e) => setRoleFilter(e.target.value)}
          className="filter-select"
        >
          <option value="All">All Roles</option>
          <option value="Admin">Admin</option>
          <option value="User">User</option>
        </select>

        <select 
          value={statusFilter} 
          onChange={(e) => setStatusFilter(e.target.value)}
          className="filter-select"
        >
          <option value="All">All Status</option>
          <option value="Active">Active</option>
          <option value="Inactive">Inactive</option>
        </select>
      </div>

      {/* Derived Info */}
      <p className="stats">
        Showing <strong>{filteredUsers.length}</strong> of <strong>{users.length}</strong> users
      </p>

      {/* Table */}
      <table className="user-table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Role</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {filteredUsers.length > 0 ? (
            filteredUsers.map((user) => (
              <tr key={user.id}>
                <td>{user.name}</td>
                <td>{user.role}</td>
                <td>
                  <span className={`status-badge ${user.active ? 'active' : 'inactive'}`}>
                    {user.active ? 'Active' : 'Inactive'}
                  </span>
                </td>
                <td>
                  <button 
                    onClick={() => toggleUserStatus(user.id)}
                    className="toggle-btn"
                  >
                    {user.active ? 'Deactivate' : 'Activate'}
                  </button>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4" style={{ textAlign: "center" }}>No users found</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default App;